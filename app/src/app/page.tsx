import { getTopics, getCommitments, getMetrics } from '../lib/data'

export default async function Home() {
  const topics = await getTopics()
  const commitments = await getCommitments()
  const metrics = await getMetrics()

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-gradient-to-r from-blue-600 to-indigo-700 text-white">
        <div className="absolute inset-0 bg-grid-white/[0.05] bg-[size:20px_20px]"></div>
        <div className="relative max-w-6xl mx-auto px-6 py-24">
          <div className="text-center space-y-6">
            <div className="inline-block px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full text-sm font-medium mb-4">
              NADA 20 Group GC06 • January 2026
            </div>
            <h1 className="text-6xl font-bold tracking-tight">
              Executive Intelligence Brief
            </h1>
            <p className="text-2xl text-blue-100 max-w-2xl mx-auto">
              Two Days. 40+ Operators. One Pattern.
            </p>
            <div className="flex gap-4 justify-center pt-4">
              <div className="px-6 py-3 bg-white/20 backdrop-blur-sm rounded-lg">
                <div className="text-3xl font-bold">{topics.length}</div>
                <div className="text-sm text-blue-100">Topics</div>
              </div>
              <div className="px-6 py-3 bg-white/20 backdrop-blur-sm rounded-lg">
                <div className="text-3xl font-bold">{commitments.length}</div>
                <div className="text-sm text-blue-100">Commitments</div>
              </div>
              <div className="px-6 py-3 bg-white/20 backdrop-blur-sm rounded-lg">
                <div className="text-3xl font-bold">{metrics.length}</div>
                <div className="text-sm text-blue-100">Metrics</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Topics Section */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            What the Room Agreed On
          </h2>
          <p className="text-xl text-gray-600">
            {topics.length} canonical topics emerged from the discussion
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {topics.map((topic) => (
            <div 
              key={topic.id} 
              className="group bg-white p-6 rounded-2xl shadow-sm border border-gray-200 hover:shadow-xl hover:scale-[1.02] hover:border-blue-300 transition-all duration-300 cursor-pointer"
            >
              <div className="flex justify-between items-start mb-3">
                <h3 className="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
                  {topic.topic}
                </h3>
                <div className="flex items-center gap-2">
                  <div className="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-blue-500 to-indigo-600 transition-all duration-500"
                      style={{ width: `${topic.confidence * 100}%` }}
                    ></div>
                  </div>
                  <span className="text-sm font-semibold text-gray-600">
                    {(topic.confidence * 100).toFixed(0)}%
                  </span>
                </div>
              </div>
              <p className="text-gray-600 mb-3 leading-relaxed">{topic.definition}</p>
              <div className="flex items-center justify-between">
                <span className="inline-block px-3 py-1 bg-blue-50 text-blue-700 text-sm font-medium rounded-full">
                  {topic.status}
                </span>
                <span className="text-sm text-gray-400">
                  {topic.evidence?.count || 0} evidence chunks
                </span>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Visualizations Section */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Topic Analysis
          </h2>
          <p className="text-xl text-gray-600">
            Interactive visualization of discussion patterns
          </p>
        </div>
        <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-200 hover:shadow-2xl transition-shadow duration-300">
          <iframe
            src="https://easyazauclbtxgkxyfbe.supabase.co/storage/v1/object/public/assets/charts/topic_gravity_map.html"
            className="w-full h-[600px] border-0 rounded-lg"
            title="Topic Gravity Map"
          />
        </div>
      </section>

      {/* Commitments Section */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Dealer Commitments
          </h2>
          <p className="text-xl text-gray-600">
            {commitments.length} commitments captured from the meeting
          </p>
        </div>
        
        <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-200 mb-8 hover:shadow-2xl transition-shadow duration-300">
          <iframe
            src="https://easyazauclbtxgkxyfbe.supabase.co/storage/v1/object/public/assets/charts/commitment_matrix.html"
            className="w-full h-[500px] border-0 rounded-lg"
            title="Commitment Matrix"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {commitments.map((commitment) => (
            <div 
              key={commitment.id} 
              className="bg-white p-6 rounded-xl shadow-sm border border-gray-200 hover:shadow-lg hover:border-blue-300 hover:scale-[1.02] transition-all duration-300"
            >
              <div className="flex items-start gap-4">
                <span className="flex-shrink-0 w-12 h-12 flex items-center justify-center bg-gradient-to-br from-blue-500 to-indigo-600 text-white font-bold rounded-lg text-sm">
                  {commitment.dealer_code}
                </span>
                <div className="flex-1">
                  <p className="text-sm font-bold text-blue-600 mb-2">
                    {commitment.theme}
                  </p>
                  <p className="text-gray-700 leading-relaxed">{commitment.statement}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Metrics Section */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <div className="text-center mb-12">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Performance Metrics
          </h2>
          <p className="text-xl text-gray-600">
            Key performance indicators across the group
          </p>
        </div>
        
        <div className="bg-white p-8 rounded-2xl shadow-lg border border-gray-200 mb-8 hover:shadow-2xl transition-shadow duration-300">
          <iframe
            src="https://easyazauclbtxgkxyfbe.supabase.co/storage/v1/object/public/assets/charts/metrics_variance.html"
            className="w-full h-[500px] border-0 rounded-lg"
            title="Metrics Variance"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {metrics.map((metric) => (
            <div 
              key={metric.id} 
              className="bg-gradient-to-br from-white to-blue-50 p-8 rounded-2xl shadow-sm border border-gray-200 hover:shadow-xl hover:scale-[1.02] transition-all duration-300"
            >
              <h3 className="text-2xl font-bold text-gray-900 mb-6">
                {metric.name}
              </h3>
              <div className="space-y-4">
                <div className="flex justify-between items-center">
                  <span className="text-gray-600 font-medium">Median:</span>
                  <span className="text-3xl font-bold text-blue-600">
                    {metric.median} <span className="text-lg text-gray-500">{metric.units}</span>
                  </span>
                </div>
                <div className="pt-4 border-t border-gray-200">
                  <div className="flex justify-between text-sm mb-2">
                    <span className="text-gray-500">Low</span>
                    <span className="text-gray-500">High</span>
                  </div>
                  <div className="relative h-3 bg-gray-200 rounded-full overflow-hidden">
                    <div className="absolute inset-0 bg-gradient-to-r from-red-400 via-yellow-400 to-green-400"></div>
                  </div>
                  <div className="flex justify-between text-sm mt-2 font-semibold">
                    <span className="text-red-600">{metric.low}</span>
                    <span className="text-green-600">{metric.high}</span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gradient-to-r from-gray-900 to-gray-800 text-white mt-24">
        <div className="max-w-6xl mx-auto px-6 py-12">
          <div className="text-center">
            <p className="text-lg font-medium mb-2">
              Built for NADA 20 Group GC06 - January 2026
            </p>
            <p className="text-gray-400">
              ServiceSync AI © 2026 • Powered by AI-driven intelligence
            </p>
          </div>
        </div>
      </footer>
    </main>
  )
}
