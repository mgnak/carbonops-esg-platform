const MetricCard = ({ title, value }) => {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

      <p className="text-slate-400 text-sm mb-2">
        {title}
      </p>

      <h2 className="text-3xl font-bold">
        {value}
      </h2>

    </div>
  );
};

export default MetricCard;