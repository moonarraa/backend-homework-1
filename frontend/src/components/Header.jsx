import { Button } from "@shadcn/ui/button";

export default function Header() {
  return (
    <header className="flex justify-between items-center p-4 border-b">
      <span className="text-2xl font-bold text-red-600">zapis</span>
      <div className="flex items-center gap-2">
        <span className="text-gray-600">Алматы</span>
        <Button variant="outline">Войти</Button>
      </div>
    </header>
  );
} 