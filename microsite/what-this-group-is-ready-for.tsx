export default function WhatThisGroupIsReadyFor() {
  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">

        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          What This Group Is Actually Ready For
        </h2>
        <p className="text-base text-gray-400 mb-16">
          The pattern is already visible.
        </p>

        {/* Before / After timeline */}
        <div className="w-full mb-16">
          <svg viewBox="0 0 100 52" className="w-full h-auto" style={{ maxHeight: 260 }}>

            {/* Labels */}
            {["Before", "After"].map((label, i) => (
              <text
                key={label}
                x="2" y={i === 0 ? 14 : 38}
                fontSize="2.2" fill="#9ca3af"
                fontFamily="ui-sans-serif, system-ui, sans-serif"
              >
                {label}
              </text>
            ))}

            {/* ── BEFORE row ── */}
            {/* Decision node */}
            <circle cx="20" cy="14" r="4" fill="white" stroke="#9ca3af" strokeWidth="0.5" />
            <text x="20" y="14" textAnchor="middle" dominantBaseline="middle" fontSize="2" fill="#374151" fontFamily="ui-sans-serif, system-ui, sans-serif">Decision</text>

            {/* Drift line — long dashed */}
            <line x1="24.2" y1="14" x2="62" y2="14" stroke="#d1d5db" strokeWidth="0.5" strokeDasharray="1.5 1" />
            <text x="43" y="11.5" textAnchor="middle" fontSize="2" fill="#d1d5db" fontFamily="ui-sans-serif, system-ui, sans-serif">Drift</text>

            {/* Next Meeting node */}
            <circle cx="66" cy="14" r="5.5" fill="white" stroke="#d1d5db" strokeWidth="0.5" strokeDasharray="1 0.6" />
            <text x="66" y="14" textAnchor="middle" dominantBaseline="middle" fontSize="2" fill="#9ca3af" fontFamily="ui-sans-serif, system-ui, sans-serif">Next Meeting</text>

            {/* ── AFTER row ── */}
            {/* Decision node */}
            <circle cx="20" cy="38" r="4" fill="white" stroke="#6b7280" strokeWidth="0.5" />
            <text x="20" y="38" textAnchor="middle" dominantBaseline="middle" fontSize="2" fill="#374151" fontFamily="ui-sans-serif, system-ui, sans-serif">Decision</text>

            {/* Solid line to Reinforcement */}
            <line x1="24.2" y1="38" x2="41.8" y2="38" stroke="#6b7280" strokeWidth="0.6" />

            {/* Reinforcement node */}
            <circle cx="46" cy="38" r="5.5" fill="white" stroke="#6b7280" strokeWidth="0.5" />
            <text x="46" y="38" textAnchor="middle" dominantBaseline="middle" fontSize="2" fill="#374151" fontFamily="ui-sans-serif, system-ui, sans-serif">Reinforcement</text>

            {/* Solid line to Adjustment */}
            <line x1="51.5" y1="38" x2="63.8" y2="38" stroke="#6b7280" strokeWidth="0.6" />

            {/* Adjustment node */}
            <circle cx="68" cy="38" r="4.5" fill="white" stroke="#6b7280" strokeWidth="0.5" />
            <text x="68" y="38" textAnchor="middle" dominantBaseline="middle" fontSize="2" fill="#374151" fontFamily="ui-sans-serif, system-ui, sans-serif">Adjustment</text>

          </svg>
        </div>

        <p className="text-base text-gray-700">
          The next advantage won't come from more meetings or more tools.
        </p>
        <p className="text-base text-gray-400 italic mt-1">
          It will come from shortening the distance between intent and execution.
        </p>

      </div>
    </section>
  )
}
