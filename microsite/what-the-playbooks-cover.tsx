const playbooks = [
  {
    title: "Service Advisor Onboarding",
    type: "Orientation Tool",
    items: [
      "Dealership & OEM policies walkthrough",
      "DMS logins and warranty claims process",
      "Road to the sale — write-up to delivery",
      "Phone etiquette and customer communication standards",
      "MPI presentation and declined repair follow-up",
    ],
  },
  {
    title: "Advisor Best Practices",
    type: "Checklist · 50 items",
    items: [
      "Pre-pull service history before customer arrives",
      "Vehicle walkaround with every customer",
      "MPI attached to every RO",
      "Status update promised and delivered",
      "Next appointment scheduled at pickup",
    ],
  },
  {
    title: "How to Increase Hours per RO",
    type: "7-Step Process",
    items: [
      "Primary & secondary menu — train with role play",
      "Video MPI for every vehicle",
      "Present payment options",
      "Pre-sell from BDC before arrival",
      "Walk around, check history, ask for the sale",
    ],
  },
  {
    title: "Sales-to-Service Handoff Script",
    type: "Word Track",
    items: [
      "Factory-trained technicians introduction",
      "Genuine GM parts and diagnostic tools",
      "Competitive pricing positioning",
      "Resale value and maintenance records pitch",
      "First appointment scheduled before customer leaves",
    ],
  },
  {
    title: "Special Order Parts (SOR) Process",
    type: "Workflow · 7 Steps",
    items: [
      "Order part → part arrives → log to spreadsheet",
      "BDC calls customer and books appointment",
      "Vehicle comes in, part installed",
      "Remove from spreadsheet on completion",
      "Parts held 60 days, then returned or sold",
    ],
  },
  {
    title: "Menu Pricing Structure",
    type: "SOP",
    items: [
      "Oil changes, filters, wipers — fixed price",
      "Brake fluid, transmission, coolant flushes",
      "Differential and transfer case services",
      "Fuel injection and induction services",
      "Four-wheel alignment",
    ],
  },
]

export default function WhatThePlaybooksAlreadyCover() {
  return (
    <section className="bg-white py-32 border-t border-gray-100">
      <div className="max-w-3xl mx-auto px-12">

        <h2 className="text-3xl font-light tracking-tight text-gray-900 mb-3">
          What the Playbooks Already Cover
        </h2>
        <p className="text-base text-gray-400 mb-16">
          Advisor onboarding, SOPs, scripts, checklists, workflows
        </p>

        {/* Scrollable card row */}
        <div className="flex gap-5 overflow-x-auto pb-4 mb-16 -mx-2 px-2">
          {playbooks.map((p) => (
            <div
              key={p.title}
              className="flex-shrink-0 w-64 border border-gray-200 rounded-lg p-6"
            >
              <p className="text-xs text-gray-400 uppercase tracking-widest mb-2">{p.type}</p>
              <h3 className="text-sm font-medium text-gray-900 mb-4 leading-snug">{p.title}</h3>
              <ul className="space-y-2">
                {p.items.map((item) => (
                  <li key={item} className="flex items-start gap-2 text-xs text-gray-500 leading-snug">
                    <span className="mt-1.5 w-1 h-1 rounded-full bg-gray-300 flex-shrink-0" />
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <p className="text-base text-gray-500">
          The industry already knows how to run a high-performing service operation.
        </p>
        <p className="text-base text-gray-400 italic mt-1">
          Knowledge is not the constraint.
        </p>

      </div>
    </section>
  )
}
