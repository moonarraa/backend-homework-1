import { useState } from "react";
import Header from "./components/Header";
import AISearchBar from "./components/AISearchBar";
import SalonResults from "./components/SalonResults";

export default function App() {
  const [salons, setSalons] = useState([]);

  const handleSearch = async (query) => {
    try {
      const response = await fetch(`http://localhost:8000/api/salons/search`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      if (!response.ok) throw new Error("Ошибка загрузки");
      const data = await response.json();
      setSalons(data);
    } catch (err) {
      setSalons([]);
      alert(err.message || "Ошибка поиска");
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main>
        <AISearchBar onSearch={handleSearch} />
        <SalonResults salons={salons} />
      </main>
    </div>
  );
}
