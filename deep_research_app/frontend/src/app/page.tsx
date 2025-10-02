'use client';

import { useState } from 'react';

export default function Home() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    const response = await fetch('/api/research', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });
    const data = await response.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <h1 className="text-4xl font-bold mb-8">Deep Research</h1>
      <div className="w-full max-w-md">
        <div className="flex items-center border-b-2 border-teal-500 py-2">
          <input
            className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
            type="text"
            placeholder="Enter your research query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
            type="button"
            onClick={handleSearch}
            disabled={loading}
          >
            {loading ? 'Researching...' : 'Research'}
          </button>
        </div>
      </div>

      {result && (
        <div className="mt-8 w-full max-w-4xl p-8 bg-white rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold mb-4 text-gray-800">Research Results</h2>
          <div className="text-gray-700">
            <p className="mb-4">
              <span className="font-bold">Query:</span> {result.query}
            </p>
            <p className="mb-4">
              <span className="font-bold">Subagents:</span> {result.subagents}
            </p>
            <p className="mb-4">
              <span className="font-bold">Total Sources:</span> {result.total_sources}
            </p>
            <div
              className="prose mt-4"
              dangerouslySetInnerHTML={{ __html: result.synthesis.replace(/\n/g, '<br />') }}
            />
          </div>
        </div>
      )}
    </main>
  );
}
