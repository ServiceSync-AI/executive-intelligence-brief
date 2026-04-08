// Dealer footprint data — anonymized by code only
// Scale derived from absorption CSV (service + parts combined as proxy for volume)
// Market type inferred from proficiency spread and multi-meeting references
const dealers = [
  { code: "01", scale: 2, market: "suburban" },
  { code: "02", scale: 2, market: "urban" },
  { code: "04", scale: 3, market: "suburban" },
  { code: "05", scale: 1, market: "rural" },
  { code: "06", scale: 3, market: "urban" },
  { code: "07", scale: 1, market: "rural" },
  { code: "11", scale: 2, market: "suburban" },
  { code: "12", scale: 2, market: "urban" },
  { code: "14", scale: 2, market: "suburban" },
  { code: "16", scale: 3, market: "urban" },
  { code: "17", scale: 1, market: "rural" },
  { code: "20", scale: 2, market: "suburban" },
  { code: "21", scale: 2, market: "suburban" },
  { code: "23", scale: 1, market: "rural" },
  { code: "24", scale: 3, market: "urban" },
  { code: "26", scale: 3, market: "multi-rooftop" },
  { code: "27", scale: 2, market: "suburban" },
  { code: "28", scale: 3, market: "multi-rooftop" },
  { code: "41", scale: 3, market: "multi-rooftop" },
]

const marketColor: Record<string, string> = {
  "urban":         "bg-gray-800",
  "suburban":      "bg-gray-400",
  "rural":         "bg-gray-300",
  "multi-rooftop": "bg-gray-600",
}

const scaleSize: Record<number, string> = {
  1: "w-3 h-3",
  2: "w-5 h-5",
  3: "w-7 h-7",
}

export default function TheRoom() {
  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">

        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          The Room
        </h2>
        <p className="text-base text-gray-400 mb-16">
          19 dealer organizations · single-point and multi-rooftop · mixed markets
        </p>

        {/* Dot matrix */}
        <div className="flex flex-wrap gap-5 items-center mb-6">
          {dealers.map((d) => (
            <div
              key={d.code}
              title={`Dealer ${d.code} · ${d.market}`}
              className={`rounded-full ${scaleSize[d.scale]} ${marketColor[d.market]} opacity-80`}
            />
          ))}
        </div>

        {/* Legend */}
        <div className="flex flex-wrap gap-6 mb-16 text-xs text-gray-400">
          <span className="flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-gray-800" /> Urban
          </span>
          <span className="flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-gray-600" /> Multi-rooftop
          </span>
          <span className="flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-gray-400" /> Suburban
          </span>
          <span className="flex items-center gap-2">
            <span className="inline-block w-2 h-2 rounded-full bg-gray-300" /> Rural
          </span>
          <span className="flex items-center gap-2 ml-4 border-l border-gray-200 pl-4">
            Dot size = relative scale
          </span>
        </div>

        <p className="text-sm text-gray-400 italic">
          Insights drawn from a structurally diverse operator group.
        </p>

      </div>
    </section>
  )
}
