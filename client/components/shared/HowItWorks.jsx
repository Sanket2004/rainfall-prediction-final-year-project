import { MapPin, CloudRain, Zap } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const steps = [
  {
    title: "Realtime Location Data",
    description:
      "Specify your location and the date for which you need the rainfall prediction.",
    icon: MapPin,
  },
  {
    title: "Input Weather Metrics",
    description:
      "Provide detailed weather metrics for more accurate prediction results.",
    icon: CloudRain,
  },
  {
    title: "Get Instant Prediction",
    description:
      "Receive your rainfall prediction immediately based on the provided data.",
    icon: Zap,
  },
];

export default function HowItWorks() {
  return (
    <section id="how-it-works" className="py-12 scroll-mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-10">
          <h2 className="text-base text-blue-600 font-semibold tracking-wide uppercase">
            How It Works
          </h2>
          <p className="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
            Three simple steps to predict rainfall
          </p>
        </div>
        <div className="grid gap-8 md:grid-cols-3">
          {steps.map((step, index) => (
            <Card
              key={index}
              className="flex flex-col items-center text-center hover:shadow-lg transition-all duration-300"
            >
              <CardHeader className="flex items-center">
                <div className="p-3 rounded-full bg-blue-100 inline-block mb-4 w-max">
                  <step.icon className="w-6 h-6 text-blue-600" />
                </div>
                <CardTitle className="text-xl font-semibold">
                  {step.title}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600">{step.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
