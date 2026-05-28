// import React from 'react';
import MainLayout from '../layouts/MainLayout';

// Mock data to simulate an immutable audit history fetch
const AUDIT_DATA = [
  {
    id: 102,
    status: 'Approved',
    description: 'Analyst approved diesel ingestion row',
    type: 'success', // maps to green
  },
  {
    id: 88,
    status: 'Flagged',
    description: 'Unknown unit mismatch detected',
    type: 'warning', // maps to yellow
  },
];

const AuditLogs = () => {
  // Helper function to dynamically assign border colors based on status type
  const getBorderColor = (type) => {
    switch (type) {
      case 'success':
        return 'border-green-500';
      case 'warning':
        return 'border-yellow-500';
      case 'error':
        return 'border-red-500';
      default:
        return 'border-slate-500';
    }
  };

  return (
    <MainLayout>
      {/* Header Section */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2 text-white">
          Audit Logs
        </h1>
        <p className="text-slate-400">
          Immutable analyst approval history
        </p>
      </div>

      {/* Logs Container */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-6">
        {AUDIT_DATA.map((log) => (
          <div 
            key={log.id} 
            className={`border-l-2 ${getBorderColor(log.type)} pl-4 py-2`}
          >
            <p className="font-semibold text-white">
              Record #{log.id} {log.status}
            </p>
            <p className="text-slate-400 text-sm mt-0.5">
              {log.description}
            </p>
          </div>
        ))}
      </div>
    </MainLayout>
  );
};

export default AuditLogs;