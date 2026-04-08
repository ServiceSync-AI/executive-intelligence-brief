'use client'
import { useRef } from 'react'

const topics = ["Dispatching", "HR / RO", "Lost Sales", "SOPs", "Inventory", "Digital"]

const matrix: Record<string, Record<string, number> & { quotes: Record<string, string> }> = {
  "Meeting 1": {
    Dispatching: 3, "HR / RO": 10, "Lost Sales": 2, SOPs: 6, Inventory: 12, Digital: 8,
    quotes: {
      Dispatching: "Centralized dispatch improved flow and fairness (Paul).",
      "HR / RO": "If a tech is sitting, it's a system failure.",
      "Lost Sales": "Declined service = manager opportunity (TO process).",
      SOPs: "Daily huddle & scoreboard guidance noted.",
      Inventory: "Preloading parts is huge... print weekly special order parts...",
      Digital: "QR code + digital menus idea (Alex).",
    },
  },
  "Meeting 2": {
    Dispatching: 3, "HR / RO": 6, "Lost Sales": 1, SOPs: 8, Inventory: 10, Digital: 4,
    quotes: {
      Dispatching: "Dispatch books and manual processes remain in many shops.",
      "HR / RO": "Personnel expense disparities discussed — impact on absorption.",
      "Lost Sales": "Track declines due to discounts.",
      SOPs: "Policy control and weekly reviews were emphasized.",
      Inventory: "Parts ordering accuracy reduces rental costs (Riverton SOP).",
      Digital: "PAM/AI call ideas discussed.",
    },
  },
  "Meeting 3": {
    Dispatching: 3, "HR / RO": 12, "Lost Sales": 2, SOPs: 8, Inventory: 5, Digital: 6,
    quotes: {
      Dispatching: "Used car team rework freed capacity for main shop.",
      "HR / RO": "Tool Guard and labor rate restructuring produced large productivity gains.",
      "Lost Sales": "Decline recovery queue recommended.",
      SOPs: "Onboarding and mentor program recommendations noted.",
      Inventory: "Bin counts and perpetuals discussed.",
      Digital: "Digital engagement improved inspection consistency.",
    },
  },
  "Meeting 4": {
    Dispatching: 2, "HR / RO": 15, "Lost Sales": 1, SOPs: 6, Inventory: 7, Digital: 4,
    quotes: {
      Dispatching: "Central dispatch vs team dispatch debate.",
      "HR / RO": "Peak focus on proficiency: 'Frequent walk-throughs every 30 minutes...'",
      "Lost Sales": "Manager TO on large declines.",
      SOPs: "Daily accountability and scoreboards.",
      Inventory: "Preloading & parts-runner processes.",
      Digital: "Phone/BDC issues and platform friction (DealerFX complaint).",
    },
  },
  "Meeting 5": {
    Dispatching: 3, "HR / RO": 5, "Lost Sales": 2, SOPs: 7, Inventory: 13, Digital: 10,
    quotes: {
      Dispatching: "Recon process and used-car flow.",
      "HR / RO": "Flexible schedules with guardrails discussed.",
      "Lost Sales": "Lost sales tracking and emergency purchases.",
      SOPs: "Service advisor orientation & checklists emphasized.",
      Inventory: "Special order parts are dead dollars until installed.",
      Digital: "PAM AI + QR menus and Google Business Profile optimization.",
    },
  },
}

const MAX_VAL = 15

function heatColor(v: number) {
  const ratio = Math.min(1, v / MAX_VAL)
  const g = Math.round(255 - 200 * ratio)
  return `rgb(255,${g},${g})`
}

export default function WhatTheRoomAgreedOn() {
  const meetings = Object.keys(matrix)
  const tooltipRef = useRef<HTMLDivElement>(null)

  function showTip(e: React.MouseEvent, meeting: string, topic: string, v: number) {
    const tip = tooltipRef.current
    if (!tip) return
    tip.style.display = 'block'
    tip.style.left = e.pageX + 12 + 'px'
    tip.style.top = e.pageY + 12 + 'px'
    tip.innerHTML = `<strong>${topic}</strong> — <em>${meeting}</em><br/><strong>Count:</strong> ${v}<br/><br/><em>Representative:</em><div style="margin-top:6px;color:#555">${matrix[meeting].quotes[topic]}</div>`
  }

  function hideTip() {
    if (tooltipRef.current) tooltipRef.current.style.display = 'none'
  }

  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">

        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          What the Room Agreed On
        </h2>
        <p className="text-base text-gray-400 mb-16">
          X-axis = Topics · Y-axis = Meeting Part (1–5) · Color intensity = discussion density · Hover for quotes
        </p>

        {/* Heatmap table */}
        <div className="overflow-x-auto mb-6">
          <table className="border-collapse text-xs w-full">
            <thead>
              <tr>
                <th className="border border-gray-200 bg-gray-50 px-4 py-3 text-left font-medium text-gray-500 min-w-[110px]">
                  Meeting Part
                </th>
                {topics.map(t => (
                  <th key={t} className="border border-gray-200 bg-gray-50 px-4 py-3 font-medium text-gray-500 min-w-[110px]">
                    {t}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {meetings.map(meeting => (
                <tr key={meeting}>
                  <th className="border border-gray-200 px-4 py-3 text-left font-medium text-gray-600 bg-gray-50">
                    {meeting}
                  </th>
                  {topics.map(topic => {
                    const v = matrix[meeting][topic] as number
                    return (
                      <td
                        key={topic}
                        className="border border-gray-200 px-4 py-3 text-center cursor-default"
                        style={{ background: heatColor(v) }}
                        onMouseMove={e => showTip(e, meeting, topic, v)}
                        onMouseLeave={hideTip}
                      >
                        <div className="font-bold text-gray-800">{v}</div>
                        <div className="text-gray-600 mt-0.5">{topic}</div>
                      </td>
                    )
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <p className="text-xs text-gray-400 mb-16">
          Counts are approximate mention / discussion-turn counts mapped to topics for each meeting part. (Max cell value = 15)
        </p>

        <p className="text-base text-gray-400 italic">
          The group is aligned on what matters.
        </p>

      </div>

      {/* Tooltip */}
      <div
        ref={tooltipRef}
        className="fixed hidden z-50 bg-white border border-gray-200 shadow-lg rounded p-3 text-xs text-gray-700 w-72 pointer-events-none"
        style={{ display: 'none' }}
      />
    </section>
  )
}
