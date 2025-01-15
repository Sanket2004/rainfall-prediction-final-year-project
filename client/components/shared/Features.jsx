import { Cloud, Droplets, Wind } from "lucide-react";

const features = [
  {
    name: "Accurate Predictions",
    description:
      "Using advanced algorithms and real-time data for precise forecasts.",
    icon: Cloud,
  },
  {
    name: "Detailed Metrics",
    description:
      "Comprehensive weather data including temperature, humidity, and wind speed.",
    icon: Droplets,
  },
  {
    name: "User-Friendly Interface",
    description:
      "Easy-to-use platform for both amateur and professional meteorologists.",
    icon: Wind,
  },
];

export default function Features() {
  return (
    <section id="features" className="pb-24 bg-white scroll-mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-base text-blue-600 font-semibold tracking-wide uppercase">
            Features
          </h2>
          <p className="mt-2 text-3xl leading-8 font-bold tracking-tight text-gray-900 sm:text-4xl">
            A better way to predict rainfall
          </p>
        </div>

        <div className="mt-14">
          <dl className="space-y-10 md:space-y-0 md:grid md:grid-cols-3 md:gap-x-8 md:gap-y-10">
            {features.map((feature) => (
              <div key={feature.name} className="relative">
                <dt>
                  <div className="absolute flex items-center justify-center h-12 w-12 rounded-xl bg-blue-500 text-white">
                    <feature.icon className="h-6 w-6" aria-hidden="true" />
                  </div>
                  <p className="ml-16 text-lg leading-6 font-medium text-gray-900">
                    {feature.name}
                  </p>
                </dt>
                <dd className="mt-2 ml-16 text-base text-gray-500">
                  {feature.description}
                </dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </section>
  );
}
