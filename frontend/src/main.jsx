import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './index.css'
import App from './App.jsx'
import SalonsWidgetPage from "./pages/SalonsWidgetPage";

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/salons" element={<SalonsWidgetPage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
