import Features from "@/components/shared/Features";
import Hero from "@/components/shared/Hero";
import HowItWorks from "@/components/shared/HowItWorks";
import RainFallPredictionForm from "@/components/shared/RainFallPredictionForm";

export default function Home() {
  return (
    <div>
      <Hero />
      <Features />
      <HowItWorks/>
      <RainFallPredictionForm />
    </div>
  );
}
