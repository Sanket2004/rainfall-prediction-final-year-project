import React from "react";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "../ui/sheet";
import { FaBarsStaggered } from "react-icons/fa6";
import Link from "next/link";

const Navbar = () => {
  return (
    <Sheet>
      <header className="bg-white/75 shadow-sm fixed top-0 left-0 right-0 z-50 backdrop-blur-sm">
        <div className="w-full mx-auto py-4 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <Link
            href={"/"}
            className="text-2xl font-bold text-blue-600 transition-all duration-300 hover:text-blue-600/75 "
          >
            RainCast
          </Link>
          <nav>
            <ul className=" space-x-4 itesm-center md:flex hidden">
              <li>
                <Link
                  href="#features"
                  className="text-gray-600 hover:text-blue-600 transition-all duration-300"
                >
                  Features
                </Link>
              </li>
              <li>
                <Link
                  href="#how-it-works"
                  className="text-gray-600 hover:text-blue-600 transition-all duration-300"
                >
                  How It Works
                </Link>
              </li>
              <li>
                <Link
                  href="#predict"
                  className="text-gray-600 hover:text-blue-600 transition-all duration-300"
                >
                  Predict
                </Link>
              </li>
            </ul>
            <SheetTrigger className="md:hidden flex items-center">
              <FaBarsStaggered
                size={20}
                className="text-blue-600 transition-all duration-300"
              />
            </SheetTrigger>
          </nav>
        </div>
      </header>
      <SheetContent side={"bottom"}>
        <SheetHeader className={"flex items-start"}>
          <SheetTitle className="text-2xl font-bold text-blue-600 transition-all duration-300">
            <Link href={"/"}>RainCast</Link>
          </SheetTitle>
          <SheetDescription>Weather Prediction</SheetDescription>
          <nav className="flex flex-col items-start space-y-4 pt-4">
            <Link
              href="#features"
              className="text-gray-600 hover:text-blue-600 transition-all duration-300"
            >
              Features
            </Link>
            <Link
              href="#how-it-works"
              className="text-gray-600 hover:text-blue-600 transition-all duration-300"
            >
              How It Works
            </Link>
            <Link
              href="#predict"
              className="text-gray-600 hover:text-blue-600 transition-all duration-300"
            >
              Predict
            </Link>
          </nav>
        </SheetHeader>
      </SheetContent>
    </Sheet>
  );
};

export default Navbar;
