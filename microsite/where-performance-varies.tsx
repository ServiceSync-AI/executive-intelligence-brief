// All values pulled directly from CSVs in data/nada-jan-2026/Extracted Data/
// No dealer names — codes only, sorted low to high for each metric

const metrics = [
  {
    label: "Technician Proficiency",
    unit: "%",
    low: 76,
    high: 169,
    values: [76, 76, 81, 84, 87, 87, 90, 90, 103, 105, 105, 112, 113, 117, 118, 121, 125, 169],
    source: "November Proficiency Numbers [DATA].csv",
  },
  {
    label: "Service Absorption",
    unit: "%",
    low: 14,
    high: 48,
    values: [14, 23, 24, 25, 26, 26, 27, 29, 29, 32, 33, 34, 34, 35, 38, 43, 48],
    source: "Absorption for Service and Parts [DATA].csv",
  },
  {
    label: "Parts Inventory Turn",
    unit: "%",
    low: 16,
    high: 60,
    values: [16, 19, 28, 28, 29, 31, 35, 41, 42, 44, 47, 53, 54, 59, 60, 60],
    source: "Parts Inventory $ Turn [DATA].csv",
  },
  {
    label: "Recon Days",
    unit: "days",
    low: 4,
    high: 10,
    values: [4, 5, 5, 6, 6, 7, 7, 10, 10],
    target: 3,
    source: "Used Vehicle Days to Breakeven After Recon [DATA].csv",
  },
  {
    label: "Hours per RO",
    unit: "hrs",
    low: 1.6,
    high: 3.2,
    values: [1.6, 3.2],
    note: "Quick lane vs. main shop",
    source: "Steps to Increase Hours per RO [TEXT].txt · Meeting transcripts",
  },
]

function Bar({ value, min, max, target }: { value: number; min: number; max: number; target?: number }) {
  const pct = ((value - min) / (max - min)) * 100
  const targetPct = target != null ? ((target - min) / (max - min)) * 100 : null
  return (
    <div className="relative h-1.5 bg-gray-100 rounded-full w-full">
      {targetPct != null && (
        <div
          className="absolute top-1/2 -translate-y-1/2 w-px h-3 bg-gray-400"
          style={{ left: `${targetPct}%` }}
        />
      )}
      <div
        className="absolute left-0 top-0 h-full bg-gray-400 rounded-full"
        style={{ width: `${pct}%` }}
      />
    </div>
  )
}

export default function WherePerformanceStillVaries() {
  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">

        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          Where Performance Still Varies
        </h2>
        <p className="text-base text-gray-400 mb-16">
          Across 19 dealer organizations — same group, same meeting
        </p>

        <div className="grid grid-cols-1 gap-12 mb-16">
          {metrics.map((m) => {
            const sorted = [...m.values].sort((a, b) => a - b)
            return (
              <div key={m.label}>
                <div className="flex justify-between items-baseline mb-4">
                  <span className="text-sm font-medium text-gray-700">{m.label}</span>
                  {m.note
                    ? <span className="text-xs text-gray-400">{m.note}</span>
                    : <span className="text-xs text-gray-400">
                        {m.low}{m.unit} — {m.high}{m.unit}
                        {m.target != null && <span className="ml-2 text-gray-300">· target {m.target}{m.unit}</span>}
                      </span>
                  }
                </div>
                <div className="space-y-1.5">
                  {sorted.map((v, i) => (
                    <Bar key={i} value={v} min={m.low} max={m.high} target={m.target} />
                  ))}
                </div>
                <p className="text-xs text-gray-300 mt-3">Source: {m.source}</p>
              </div>
            )
          })}
        </div>

        <p className="text-base text-gray-400 italic">
          Same knowledge. Different outcomes.
        </p>

      </div>
    </section>
  )
}
