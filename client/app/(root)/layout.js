import Footer from "@/components/shared/Footer";
import Navbar from "@/components/shared/Navbar";

export default function Home({ children }) {
  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <main className="flex-1 w-full mx-auto mt-16">{children}</main>
      <Footer />
    </div>
  );
}
