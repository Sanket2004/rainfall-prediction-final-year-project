import { Toaster } from "@/components/ui/sonner";
import "./globals.css";
import { Geist } from "next/font/google";

const geist = Geist({ subsets: ["latin"] });

export const metadata = {
  title: "RainCast",
  description:
    "RainCast is a rainfall prediction app that provides accurate weather information.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        // className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        className={geist.className}
      >
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  );
}
