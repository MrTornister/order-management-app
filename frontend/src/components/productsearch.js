import React, { useState } from 'react';
import axios from 'axios';

function ProductSearch({ products, onProductSelect }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [newProduct, setNewProduct] = useState('');

  const handleSearch = (term) => {
    setSearchTerm(term);
    const filtered = products.filter(p => 
      p.toLowerCase().includes(term.toLowerCase())
    );
    setFilteredProducts(filtered);
  };

  const handleAddProduct = async () => {
    try {
      const response = await axios.post('/api/add-product', { name: newProduct });
      onProductSelect(newProduct);
      setNewProduct('');
      setSearchTerm('');
    } catch (error) {
      console.error('Błąd dodawania produktu', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Wyszukaj produkt"
        className="w-full p-2 border"
      />
      
      {filteredProducts.map((product, index) => (
        <div 
          key={index} 
          onClick={() => onProductSelect(product)}
          className="cursor-pointer hover:bg-gray-100 p-2"
        >
          {product}
        </div>
      ))}

      {filteredProducts.length === 0 && searchTerm && (
        <div>
          <p>Nie znaleziono produktu</p>
          <input
            type="text"
            value={newProduct}
            onChange={(e) => setNewProduct(e.target.value)}
            placeholder="Nazwa nowego produktu"
            className="w-full p-2 border"
          />
          <button 
            onClick={handleAddProduct}
            className="w-full p-2 bg-green-500 text-white"
          >
            Dodaj nowy produkt
          </button>
        </div>
      )}
    </div>
  );
}

export default ProductSearch;
