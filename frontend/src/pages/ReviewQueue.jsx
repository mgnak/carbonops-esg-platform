import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";
import ScopeBadge from "../components/ScopeBadge";

import { api } from "../api/axios";

const ReviewQueue = () => {

  const [records, setRecords] = useState([]);

  const fetchRecords = async () => {

    const response = await api.get("/emissions/");

    setRecords(response.data);
  };

  useEffect(() => {
    fetchRecords();
  }, []);

  return (
    <MainLayout>

      <h1 className="text-4xl font-bold mb-8">
        Review Queue
      </h1>

      <div className="bg-slate-900 rounded-2xl overflow-hidden">

        <table className="w-full">

          <thead className="bg-slate-800">

            <tr>
              <th className="p-4 text-left">Scope</th>
              <th className="p-4 text-left">Activity</th>
              <th className="p-4 text-left">Raw</th>
              <th className="p-4 text-left">Normalized</th>
              <th className="p-4 text-left">CO₂e</th>
              <th className="p-4 text-left">Status</th>
            </tr>

          </thead>

          <tbody>

            {records.map((record) => (

              <tr
                key={record.id}
                className="border-t border-slate-800"
              >

                <td className="p-4">
                  <ScopeBadge scope={record.scope} />
                </td>

                <td className="p-4">
                  {record.activity_type}
                </td>

                <td className="p-4">
                  {record.raw_value} {record.raw_unit}
                </td>

                <td className="p-4">
                  {record.normalized_value}
                </td>

                <td className="p-4">
                  {record.co2e_kg}
                </td>

                <td className="p-4">
                  {record.status}
                </td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>

    </MainLayout>
  );
};

export default ReviewQueue;