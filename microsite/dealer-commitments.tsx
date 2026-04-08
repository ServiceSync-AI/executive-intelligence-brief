// Source: Take A Way's [TEXT].txt — NADA GC06 January 2026
// Themes normalized from raw commitment statements

const themes = [
  "Hours per RO",
  "Video MPI",
  "Sales-to-Service Handoff",
  "Phone / Customer Contact",
  "Parts & Inventory",
  "Labor Gross / Rate",
  "Quick Lane Separation",
]

// dealer code → theme indices they committed to
const commitments: Record<string, number[]> = {
  "41": [5],           // Alex — Quick lane labor gross %
  "28": [0, 1],        // Colleen — Hrs per RO; Mike — Video MPI
  "27": [2],           // Leith — Sales svc handoff / sublet
  "26": [4, 1, 0, 6],  // Tara — bin counts; Penny — QR codes (MPI); Heath — MPI; Laurie — Hrs per RO / separate quick
  "24": [2],           // Brandon — Sales to svc handoff; Casey — ext warranty (billing, closest to labor/rate)
  "23": [3],           // Travis — T.O. svc cust; Chris — ph call on line appts
}

const dealers = Object.keys(commitments).sort()

// theme density = total dots per theme
const density = themes.map((_, ti) =>
  dealers.reduce((sum, d) => sum + (commitments[d].includes(ti) ? 1 : 0), 0)
)
const maxDensity = Math.max(...density)

export default function DealerCommitments() {
  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">
        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          What Each Dealership Committed To
        </h2>
        <p className="text-base text-gray-400 mb-16">
          Post-meeting execution priorities captured directly from the room.
          Numbers indicate dealership codes.
        </p>

        {/* Commitment matrix */}
        <div className="overflow-x-auto mb-3">
          <table className="w-full text-xs">
            <thead>
             <tr>
                <th className="text-left font-normal text-gray-400 pb-4 pr-6 w-40">Theme</th>
                {dealers.map(d => (
                  <th key={d} className="font-normal text-gray-400 pb-4 px-3 text-center">{d}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {themes.map((theme, ti) => (
                <tr key={theme} className="border-t border-gray-100">
                  <td className="text-gray-500 py-3 pr-6 leading-snug">{theme}</td>
                  {dealers.map(d => (
                    <td key={d} className="py-3 px-3 text-center">
                      {commitments[d].includes(ti) && (
                        <span className="inline-block w-2 h-2 rounded-full bg-gray-700" />
                      )}
                    </td>
                  ))}
                </tr>
              ))}
             </tbody>
          </table>
        </div>
        <p className="text-xs text-gray-300 mb-16">
          Rows = execution themes · Columns = dealer codes · <span className="inline-block w-1.5 h-1.5 rounded-full bg-gray-400 align-middle mx-0.5" /> = commitment made by that dealership
        </p>

        {/* Theme density bars */}
        <div className="space-y-3 mb-3">
          {themes.map((theme, ti) => (
            <div key={theme} className="flex items-center gap-4">
              <span className="text-xs text-gray-400 w-40 flex-shrink-0">{theme}</span>
              <div className="flex-1 h-1.5 bg-gray-100 rounded-full">
                <div
                  className="h-full bg-gray-400 rounded-full"
                  style={{ width: `${(density[ti] / maxDensity) * 100}%` }}
                />
               </div>
               <span className="text-xs text-gray-300 w-4 text-right">{density[ti]}</span>
            </div>
          ))}
        </div>
        <p className="text-xs text-gray-300 mb-16">
          Bar length = number of dealerships that committed to each theme · Number on right = dealership count
        </p>

        <p className="text-base text-gray-500">
          Despite differences in store size and market,
        </p>
        <p className="text-base text-gray-400 italic">
          priorities converged quickly.
        </p>

      </div>
    </section>
  )
}