import { supabase } from './supabase'

export interface Topic {
  id: string
  topic: string
  definition: string
  status: string
  evidence: any
  confidence: number
}

export interface Commitment {
  id: string
  dealer_code: string
  theme: string
  statement: string
  evidence: any
}

export interface Metric {
  id: string
  name: string
  median: number
  low: number
  high: number
  units: string
  evidence: any
}

export async function getTopics(): Promise<Topic[]> {
  const { data, error } = await supabase
    .from('knowledge_topics')
    .select('*')
    .order('confidence', { ascending: false })
  
  if (error) throw error
  return data || []
}

export async function getCommitments(): Promise<Commitment[]> {
  const { data, error } = await supabase
    .from('commitments')
    .select('*')
  
  if (error) throw error
  return data || []
}

export async function getMetrics(): Promise<Metric[]> {
  const { data, error } = await supabase
    .from('metrics')
    .select('*')
  
  if (error) throw error
  return data || []
}
