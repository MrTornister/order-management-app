import React, { useState, useEffect } from 'react';
import OrderForm from './components/OrderForm';
import ProductSearch from './components/ProductSearch';
import axios from 'axios';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('/api/products');
        setProducts(response.data);
      } catch (error) {
        console.error('Błąd pobierania produktów', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">System Zamówień</h1>
      <OrderForm products={products} />
    </div>
  );
}

export default App;
