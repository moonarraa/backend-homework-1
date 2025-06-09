import { useEffect, useState } from "react";

export default function SalonsWidget() {
  const [salons, setSalons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/salons/hair")
      .then(res => {
        if (!res.ok) throw new Error("Ошибка загрузки");
        return res.json();
      })
      .then(data => {
        setSalons(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>Ошибка: {error}</div>;

  return (
    <div className="p-4 bg-white rounded shadow max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-2">Парикмахерские Алматы</h2>
      <ul>
        {salons.map((salon, idx) => (
          <li key={idx} className="mb-2">
            <div className="font-semibold">{salon.name}</div>
            <div className="text-gray-600 text-sm">{salon.address}</div>
          </li>
        ))}
      </ul>
    </div>
  );
} 