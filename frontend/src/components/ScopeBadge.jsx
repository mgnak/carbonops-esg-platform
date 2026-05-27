const ScopeBadge = ({ scope }) => {

  const colors = {
    SCOPE_1: "bg-red-500/20 text-red-300",
    SCOPE_2: "bg-yellow-500/20 text-yellow-300",
    SCOPE_3: "bg-blue-500/20 text-blue-300",
  };

  return (
    <span
      className={`px-3 py-1 rounded-full text-sm ${colors[scope]}`}
    >
      {scope}
    </span>
  );
};

export default ScopeBadge;