"use client";

export default function Footer() {
  return (
    <footer className="bg-gradient-to-t from-blue-100">
      <div className="mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between flex-col items-center">
          <div>
            <h2 className="text-2xl font-bold text-blue-600 text-center">RainCast</h2>
            <p className="mt-2 text-sm">
              Precision rainfall prediction at your fingertips
            </p>
          </div>
          <div>
            <ul className="mt-4 flex items-center gap-4 flex-wrap">
              <li>
                <a href="#features" className="hover:text-blue-400 transition-all duration-300">
                  Features
                </a>
              </li>
              <li>
                <a href="#how-it-works" className="hover:text-blue-400 transition-all duration-300">
                  How It Works
                </a>
              </li>
              <li>
                <a href="#predict" className="hover:text-blue-400 transition-all duration-300">
                  Predict
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div className="mt-4 border-t border-neutral-400/30 pt-4 text-center text-neutral-500">
          <p className="text-sm">
            &copy; {new Date().getFullYear()} RainCast. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
