const steps = ["Decision", "Owner", "Action", "Measurement", "Follow-up"]

const breakpoints = [
  { after: 0, label: "After meetings" },
  { after: 2, label: "Between departments" },
  { after: 3, label: "Between shifts" },
  { after: 3, label: "Between systems" },
]

export default function WhereExecutionBreaks() {
  // Each step is evenly spaced across a 100-unit viewBox
  const n = steps.length
  const cx = (i: number) => 10 + (i / (n - 1)) * 80
  const cy = 40

  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">

        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          Where Execution Quietly Breaks
        </h2>
        <p className="text-base text-gray-400 mb-16">
          The loop looks complete. The gaps are invisible.
        </p>

        {/* Execution loop diagram */}
        <div className="w-full mb-16">
          <svg viewBox="0 0 100 80" className="w-full h-auto" style={{ maxHeight: 320 }}>
            {/* Connecting lines — solid between steps, dashed at breakpoints */}
            {steps.map((_, i) => {
              if (i === n - 1) return null
              const x1 = cx(i) + 5.5
              const x2 = cx(i + 1) - 5.5
              const isBreak = breakpoints.some(b => b.after === i)
              return (
                <line
                  key={i}
                  x1={x1} y1={cy} x2={x2} y2={cy}
                  stroke={isBreak ? "#d1d5db" : "#9ca3af"}
                  strokeWidth={isBreak ? "0.4" : "0.6"}
                  strokeDasharray={isBreak ? "1.2 0.8" : undefined}
                />
              )
            })}

            {/* Step nodes */}
            {steps.map((label, i) => (
              <g key={label}>
                <circle cx={cx(i)} cy={cy} r="5.5" fill="white" stroke="#9ca3af" strokeWidth="0.5" />
                <text
                  x={cx(i)} y={cy}
                  textAnchor="middle" dominantBaseline="middle"
                  fontSize="2.2" fill="#374151"
                  fontFamily="ui-sans-serif, system-ui, sans-serif"
                >
                  {label}
                </text>
              </g>
            ))}

            {/* Breakpoint markers */}
            {[
              { after: 0, label: "After meetings" },
              { after: 2, label: "Between\ndepts & shifts" },
              { after: 3, label: "Between\nsystems" },
            ].map(({ after, label }) => {
              const x = (cx(after) + cx(after + 1)) / 2
              return (
                <g key={label}>
                  <line x1={x} y1={cy - 8} x2={x} y2={cy - 5.5} stroke="#d1d5db" strokeWidth="0.4" />
                  {label.split("\n").map((line, li) => (
                    <text
                      key={li}
                      x={x} y={cy - 10 - li * 3}
                      textAnchor="middle"
                      fontSize="2" fill="#9ca3af"
                      fontFamily="ui-sans-serif, system-ui, sans-serif"
                    >
                      {line}
                    </text>
                  ))}
                </g>
              )
            })}
          </svg>
        </div>

        {/* Breakpoint list */}
        <ul className="space-y-2 mb-16 text-sm text-gray-400">
          {["After meetings", "Between departments", "Between shifts", "Between systems"].map(item => (
            <li key={item} className="flex items-center gap-3">
              <span className="w-4 border-t border-dashed border-gray-300 flex-shrink-0" />
              {item}
            </li>
          ))}
        </ul>

        <p className="text-base text-gray-700">
          Most failures occur between steps, not within them.
        </p>
        <p className="text-base text-gray-400 italic mt-1">
          The system doesn't remember. People are forced to.
        </p>

      </div>
    </section>
  )
}
