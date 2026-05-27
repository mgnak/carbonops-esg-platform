import MainLayout from '../layouts/MainLayout'

const AuditLogs = () => {

  return (
    <MainLayout>

      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2">
          Audit Logs
        </h1>

        <p className="text-slate-400">
          Immutable analyst approval history
        </p>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

        <div className="border-l-2 border-green-500 pl-4 py-2 mb-6">
          <p className="font-semibold">
            Record #102 Approved
          </p>

          <p className="text-slate-400 text-sm">
            Analyst approved diesel ingestion row
          </p>
        </div>

        <div className="border-l-2 border-yellow-500 pl-4 py-2">
          <p className="font-semibold">
            Record #88 Flagged
          </p>

          <p className="text-slate-400 text-sm">
            Unknown unit mismatch detected
          </p>
        </div>

      </div>

    </MainLayout>
  )
}

export default AuditLogs