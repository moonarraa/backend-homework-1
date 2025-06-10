import { useState } from "react";
import { Button } from "@shadcn/ui/button";
import { Input } from "@shadcn/ui/input";

export default function AISearchBar({ onSearch }) {
  const [query, setQuery] = useState("");

  return (
    <div className="flex flex-col items-center gap-4 mt-10">
      <Input
        className="w-full max-w-xl"
        placeholder="Опишите что вам нужно... (например: 'Хочу маникюр рядом с Достык Плаза завтра в 17:00')"
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <Button className="w-full max-w-xl" onClick={() => onSearch(query)}>
        Найти
      </Button>
    </div>
  );
} 