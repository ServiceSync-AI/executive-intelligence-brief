import Hero from './hero'
import TheRoom from './the-room'
import WhatTheRoomAgreedOn from './what-the-room-agreed-on'
import WhatThePlaybooksCover from './what-the-playbooks-cover'
import WherePerformanceStillVaries from './where-performance-varies'
import DealerCommitments from './dealer-commitments'
import WhereExecutionBreaks from './where-execution-breaks'
import WhatThisGroupIsReadyFor from './what-this-group-is-ready-for'
import Closing from './closing'

export default async function Home() {
  return (
    <main>
      <Hero />
      <TheRoom />
      <WhatTheRoomAgreedOn />
      <WhatThePlaybooksCover />
      <WherePerformanceStillVaries />
      <DealerCommitments />
      <WhereExecutionBreaks />
      <WhatThisGroupIsReadyFor />
      <Closing />
    </main>
  )
}