import SalonsWidget from "../components/SalonsWidget";

export default function SalonsWidgetPage() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center">
      <h1 className="text-2xl font-bold mb-6">Список парикмахерских</h1>
      <SalonsWidget />
    </div>
  );
} 