import { getTopics, getCommitments, getMetrics } from './lib/data'

export default async function Home() {
  const topics = await getTopics()
  const commitments = await getCommitments()
  const metrics = await getMetrics()

  return (
    <main className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <section className="bg-white border-b">
        <div className="max-w-4xl mx-auto px-6 py-16">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Executive Intelligence Brief
          </h1>
          <p className="text-xl text-gray-600">
            NADA GC06 - January 2026
          </p>
          <p className="text-lg text-gray-500 mt-4">
            Two Days. 40+ Operators. One Pattern.
          </p>
        </div>
      </section>

      {/* Topics Section */}
      <section className="max-w-4xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">
          What the Room Agreed On
        </h2>
        <p className="text-gray-600 mb-8">
          {topics.length} canonical topics emerged from the discussion
        </p>
        
        <div className="space-y-4">
          {topics.map((topic) => (
            <div key={topic.id} className="bg-white p-6 rounded-lg shadow-sm border">
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-xl font-semibold text-gray-900">
                  {topic.topic}
                </h3>
                <span className="text-sm text-gray-500">
                  {(topic.confidence * 100).toFixed(0)}% confidence
                </span>
              </div>
              <p className="text-gray-600 mb-2">{topic.definition}</p>
              <p className="text-sm text-gray-500">{topic.status}</p>
              <p className="text-xs text-gray-400 mt-2">
                Evidence: {topic.evidence?.count || 0} chunks
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Visualizations Section */}
      <section className="max-w-4xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">
          Topic Analysis
        </h2>
        <div className="bg-white p-6 rounded-lg shadow-sm border">
          <iframe
            src="https://easyazauclbtxgkxyfbe.supabase.co/storage/v1/object/public/assets/charts/topic_gravity_map.html"
            className="w-full h-[600px] border-0"
            title="Topic Gravity Map"
          />
        </div>
      </section>

      {/* Commitments Section */}
      <section className="max-w-4xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">
          Dealer Commitments
        </h2>
        <p className="text-gray-600 mb-8">
          {commitments.length} commitments captured from the meeting
        </p>
        
        <div className="bg-white p-6 rounded-lg shadow-sm border mb-8">
          <iframe
            src="https://easyazauclbtxgkxyfbe.supabase.co/storage/v1/object/public/assets/charts/commitment_matrix.html"
            className="w-full h-[500px] border-0"
            title="Commitment Matrix"
          />
        </div>

        <div className="space-y-3">
          {commitments.map((commitment) => (
            <div key={commitment.id} className="bg-white p-4 rounded-lg shadow-sm border">
              <div className="flex items-start gap-4">
                <span className="text-sm font-mono text-gray-500">
                  {commitment.dealer_code}
                </span>
                <div className="flex-1">
                  <p className="text-sm font-medium text-gray-700 mb-1">
                    {commitment.theme}
                  </p>
                  <p className="text-gray-600">{commitment.statement}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Metrics Section */}
      <section className="max-w-4xl mx-auto px-6 py-12">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">
          Performance Metrics
        </h2>
        
        <div className="bg-white p-6 rounded-lg shadow-sm border mb-8">
          <iframe
            src="https://easyazauclbtxgkxyfbe.supabase.co/storage/v1/object/public/assets/charts/metrics_variance.html"
            className="w-full h-[500px] border-0"
            title="Metrics Variance"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {metrics.map((metric) => (
            <div key={metric.id} className="bg-white p-6 rounded-lg shadow-sm border">
              <h3 className="text-lg font-semibold text-gray-900 mb-3">
                {metric.name}
              </h3>
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span className="text-gray-600">Median:</span>
                  <span className="font-medium">{metric.median} {metric.units}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Range:</span>
                  <span className="font-medium">{metric.low} - {metric.high}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-white border-t mt-16">
        <div className="max-w-4xl mx-auto px-6 py-8">
          <p className="text-sm text-gray-500">
            Built for NADA 20 Group GC06 - January 2026
          </p>
          <p className="text-xs text-gray-400 mt-2">
            ServiceSync AI © 2026
          </p>
        </div>
      </footer>
    </main>
  )
}
