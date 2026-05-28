// import MainLayout from "../layouts/MainLayout";
// import MetricCard from "../components/MetricCard";

// const Dashboard = () => {

//   return (
//     <MainLayout>

//       <div className="mb-8">

//         <h1 className="text-4xl font-bold mb-2">
//           ESG Emissions Dashboard
//         </h1>

//         <p className="text-slate-400">
//           Enterprise carbon accounting workflow
//         </p>

//       </div>

//       <div className="grid grid-cols-4 gap-6">

//         <MetricCard
//           title="Total Records"
//           value="1,248"
//         />

//         <MetricCard
//           title="Approved"
//           value="1,042"
//         />

//         <MetricCard
//           title="Flagged"
//           value="24"
//         />

//         <MetricCard
//           title="Total tCO₂e"
//           value="492.4"
//         />

//       </div>

//     </MainLayout>
//   );
// };

// export default Dashboard;



import UploadCard from '../components/UploadCard'


export default function Dashboard() {

  return (
    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold mb-8">
        CarbonOps ESG Dashboard
      </h1>

      <div className="grid grid-cols-3 gap-6">

        <UploadCard />

      </div>

    </div>
  )
}