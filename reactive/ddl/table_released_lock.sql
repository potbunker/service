-- Table: public.lock

-- DROP TABLE public.lock;

CREATE TABLE public.released_lock
(
  lock_domain text NOT NULL,
  hostname text NOT NULL,
  process_id integer NOT NULL,
  acquired_at timestamp with time zone NOT NULL,
  released_at timestamp with time zone NOT NULL
)
WITH (
  OIDS=FALSE
);

ALTER TABLE public.released_lock
  OWNER TO event_store_dev;
