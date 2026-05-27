import {
  LayoutDashboard,
  Upload,
  ShieldCheck,
  FileSearch,
} from "lucide-react";

import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="w-72 bg-slate-900 border-r border-slate-800 p-6">

      <h1 className="text-2xl font-bold mb-10">
        CarbonOps
      </h1>

      <div className="space-y-4">

        <Link
          to="/"
          className="flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800"
        >
          <LayoutDashboard size={20} />
          Dashboard
        </Link>

        <Link
          to="/upload"
          className="flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800"
        >
          <Upload size={20} />
          Upload Center
        </Link>

        <Link
          to="/review"
          className="flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800"
        >
          <ShieldCheck size={20} />
          Review Queue
        </Link>

        <Link
          to="/audit"
          className="flex items-center gap-3 p-3 rounded-lg hover:bg-slate-800"
        >
          <FileSearch size={20} />
          Audit Logs
        </Link>

      </div>

    </div>
  );
};

export default Sidebar;