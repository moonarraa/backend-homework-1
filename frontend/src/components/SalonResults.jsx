export default function SalonResults({ salons }) {
  if (!salons || salons.length === 0) {
    return <div className="text-center text-gray-500 mt-8">Нет результатов</div>;
  }
  return (
    <ul className="max-w-xl mx-auto mt-8 space-y-4">
      {salons.map((salon, idx) => (
        <li key={idx} className="p-4 bg-white rounded shadow">
          <div className="font-semibold">{salon.name}</div>
          <div className="text-gray-600 text-sm">{salon.address}</div>
        </li>
      ))}
    </ul>
  );
} 