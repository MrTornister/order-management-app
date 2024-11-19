import React, { useState } from 'react';
import ProductSearch from './ProductSearch';
import axios from 'axios';

function OrderForm({ products }) {
  const [userName, setUserName] = useState('');
  const [selectedProducts, setSelectedProducts] = useState([]);
  const [priority, setPriority] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/submit-order', {
        user_name: userName,
        products: selectedProducts,
        priority: priority
      });
      alert(`Zamówienie złożone: ${response.data.order_number}`);
    } catch (error) {
      console.error('Błąd składania zamówienia', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input 
        type="text" 
        value={userName} 
        onChange={(e) => setUserName(e.target.value)}
        placeholder="Imię i nazwisko" 
        required 
        className="w-full p-2 border"
      />
      
      <ProductSearch 
        products={products} 
        onProductSelect={(product) => setSelectedProducts([...selectedProducts, product])}
      />

      <div>
        <h3>Wybrane produkty:</h3>
        {selectedProducts.map((product, index) => (
          <div key={index}>{product}</div>
        ))}
      </div>

      <select 
        value={priority} 
        onChange={(e) => setPriority(e.target.value)}
        required 
        className="w-full p-2 border"
      >
        <option value="">Wybierz priorytet</option>
        <option value="Zostały ostatnie sztuki">Zostały ostatnie sztuki</option>
        <option value="Brak na stanie - bardzo pilne !!!">Brak na stanie - bardzo pilne !!!</option>
        <option value="Uzupełnienie magazynu">Uzupełnienie magazynu</option>
      </select>

      <button 
        type="submit" 
        className="w-full p-2 bg-blue-500 text-white"
      >
        Złóż zamówienie
      </button>
    </form>
  );
}

export default OrderForm;
