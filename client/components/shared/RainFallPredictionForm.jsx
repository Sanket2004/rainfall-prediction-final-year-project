"use client";

import React, { useState } from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "../ui/card";
import { Loader2, MapPinIcon, SunIcon, CloudRainIcon } from "lucide-react";
import { Button } from "../ui/button";
import { Label } from "../ui/label";
import { Input } from "../ui/input";
import { toast } from "sonner";

const RainFallPredictionForm = () => {
  const [formData, setFormData] = useState({
    pressure: 1025.9,
    maxtemp: 19.9,
    temparature: 18.3,
    mintemp: 16.8,
    dewpoint: 13.1,
    humidity: 72,
    cloud: 49,
    sunshine: 9.3,
    winddirection: 80,
    windspeed: 26.3,
  });
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [predicting, setpredicting] = useState(false);
  const [error, setError] = useState(null);
  const [currentWeather, setCurrentWeather] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setPrediction(null);
      setpredicting(true);
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/predict`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );
      const data = await response.json();
      setPrediction(data.rainfall);
      toast.success("Rainfall prediction successful.");
      setpredicting(false);
    } catch (err) {
      toast.error("Failed to predict rainfall.");
      setError(err.message);
      setpredicting(false);
    }
  };

  const fetchWeatherData = async () => {
    try {
      setLoading(true);
      setError(null);
      setPrediction(null);

      navigator.geolocation.getCurrentPosition(async (position) => {
        const { latitude, longitude } = position.coords;

        const apiKey = "879534249ba8994e78dc54c905135a09";
        const response = await fetch(
          `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${apiKey}`
        );

        if (!response.ok) {
          toast.error("Failed to fetch weather data.");
          setLoading(false);
          throw new Error("Failed to fetch weather data.");
        }

        const data = await response.json();

        setCurrentWeather({
          city: data.name,
          temperature: data.main.temp,
          description: data.weather[0].description,
          icon: `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`,
          humidity: data.main.humidity,
          windSpeed: data.wind.speed,
        });

        setFormData({
          pressure: data.main.pressure,
          maxtemp: data.main.temp_max,
          temparature: data.main.temp,
          mintemp: data.main.temp_min,
          dewpoint: data.main.temp_min, // Fallback for dew point
          humidity: data.main.humidity,
          cloud: data.clouds.all,
          sunshine: data.sunshine || 0, // Replace with fallback
          winddirection: data.wind.deg,
          windspeed: data.wind.speed,
        });

        toast.success("Weather data fetched successfully.");
        setLoading(false);
      });
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
      setLoading(false);
    }
  };

  return (
    <section id="predict" className="py-12 bg-white scroll-mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-base text-center text-blue-600 font-semibold tracking-wide uppercase">
          Predict Rainfall
        </h2>
        <p className="mt-2 text-3xl text-center mb-8 leading-8 font-bold tracking-tight text-gray-900 sm:text-4xl">
          Make Your Prediction
        </p>
        <Card className="w-full max-w-2xl mx-auto">
          <CardHeader className="flex items-center justify-between flex-row gap-2">
            <div className="flex-1">
              <CardTitle>Enter Weather Details</CardTitle>
              <CardDescription>
                Use your current location to fetch weather data
              </CardDescription>
            </div>
            <Button
              onClick={fetchWeatherData}
              disabled={loading}
              className="p-2.5"
            >
              {loading ? (
                <Loader2 className="animate-spin" size={22} />
              ) : (
                <MapPinIcon />
              )}
            </Button>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="grid grid-cols-2 gap-4">
                {Object.keys(formData).map((key) => (
                  <div className="space-y-2" key={key}>
                    <Label htmlFor={key}>
                      {key.charAt(0).toUpperCase() + key.slice(1)}
                    </Label>
                    <Input
                      id={key}
                      type="number"
                      name={key}
                      value={formData[key]}
                      onChange={handleChange}
                    />
                  </div>
                ))}
              </div>
              <Button type="submit" disabled={predicting} className="w-full">
                {predicting ? (
                  <Loader2 className="animate-spin" size={22} />
                ) : (
                  "Predict Rainfall"
                )}
              </Button>
            </form>
            {prediction && (
              <div className="mt-6 p-4 bg-blue-100 rounded-md">
                <h2 className="text-blue-600">Prediction Result</h2>
                <p>
                  {prediction === "No"
                    ? `There is no chance of rainfall in your area on ${new Date().toLocaleDateString()}`
                    : `There is a chance of rainfall in your area on ${new Date().toLocaleDateString()}`}
                </p>
              </div>
            )}
          </CardContent>
        </Card>

        {currentWeather && (
          <Card className="w-full max-w-2xl mx-auto mt-8">
            <CardHeader>
              <CardTitle>Current Weather in {currentWeather.city}</CardTitle>
            </CardHeader>
            <CardContent className="flex items-center gap-4">
              <img
                src={currentWeather.icon}
                alt={currentWeather.description}
                className="w-16 h-16"
              />
              <div>
                <p className="text-xl font-bold">
                  {currentWeather.temperature}°C
                </p>
                <p className="text-sm capitalize">
                  {currentWeather.description}
                </p>
                <p className="text-sm">Humidity: {currentWeather.humidity}%</p>
                <p className="text-sm">
                  Wind Speed: {currentWeather.windSpeed} m/s
                </p>
              </div>
            </CardContent>
          </Card>
        )}
      </div>
    </section>
  );
};

export default RainFallPredictionForm;
