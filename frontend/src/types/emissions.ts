export interface EmissionRecord {
  id: number
  scope: string
  activity_type: string
  raw_value: number
  raw_unit: string
  normalized_value: number
  normalized_unit: string
  co2e_kg: number
  status: string
}