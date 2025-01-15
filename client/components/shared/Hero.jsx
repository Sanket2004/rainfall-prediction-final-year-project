import React from "react";

const Hero = () => {
  return (
    <section className="min-h-[50vh] text-center flex justify-center items-center flex-col px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-blue-100 to-white">
      <h2 className="text-4xl font-extralight text-blue-600 sm:text-5xl sm:tracking-tight lg:text-6xl">
        Predict Rainfall with Precision
      </h2>
      <p className="mt-5 mx-auto text-xl text-gray-500">
        Use advanced meteorological data to forecast rainfall in your area.
      </p>
    </section>
  );
};

export default Hero;
