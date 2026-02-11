import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Executive Intelligence Brief - NADA GC06',
  description: 'Transform meeting artifacts into operator-grade intelligence',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
