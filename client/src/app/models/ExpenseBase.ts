/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */
import { CurrencyEnum } from "./CurrencyBase";
export type Name = string;
export type Description = string | null;
export type Amount = number;
export type Date = string;
export type CategoryId = number;
export type PlaceId = number;
export type UserId = number;


export interface ExpenseBase {
  name: Name;
  description?: Description;
  amount: Amount;
  date: Date;
  category_id: CategoryId;
  place_id: PlaceId;
  user_id: UserId;
  currency: CurrencyEnum;
  [k: string]: unknown;
}
