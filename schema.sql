CREATE TABLE result (
  "phrase" TEXT NOT NULL,
  "speaker_state" TEXT NOT NULL,
  "speaker_first" TEXT NOT NULL,
  "congress" TEXT NOT NULL,
  "title" TEXT NOT NULL,
  "origin_url" TEXT NOT NULL,
  "number" TEXT NOT NULL,
  "pages" TEXT NOT NULL,
  "volume" TEXT NOT NULL,
  "chamber" TEXT NOT NULL,
  "session" INTEGER NOT NULL,
  "speaking" TEXT NOT NULL,
  "capitolwords_url" TEXT NOT NULL,
  "speaker_party" TEXT NOT NULL,
  "date" TEXT NOT NULL,
  "bills" TEXT NOT NULL,
  "bioguide_id" TEXT NOT NULL,
  "order" TEXT NOT NULL,
  "speaker_last" TEXT NOT NULL,
  "speaker_raw" TEXT NOT NULL
);
CREATE INDEX result_date ON result ("date");
CREATE INDEX result_phrase ON result ("phrase");
