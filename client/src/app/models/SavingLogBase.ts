/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */
export type Id = number;
export type Date = string;
export type Amount = number;
export type TotalAmount = number;
export type Note = string;
export type SavingId = number;

export interface SavingLogBase {
  id: Id;
  date: string | Date;
  amount: Amount;
  total_amount: TotalAmount;
  note: Note;
  saving_id: SavingId;
  [k: string]: unknown;
}
