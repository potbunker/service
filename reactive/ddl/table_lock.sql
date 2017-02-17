-- Table: public.lock

-- DROP TABLE public.lock;

CREATE TABLE public.lock
(
  lock_domain text NOT NULL,
  hostname text NOT NULL,
  process_id integer NOT NULL,
  acquired_at timestamp with time zone NOT NULL,
  retained_at timestamp with time zone NOT NULL,
  CONSTRAINT lock_pkey PRIMARY KEY (lock_domain),
  CONSTRAINT uniq_lock UNIQUE (lock_domain, hostname, process_id)
)
WITH (
  OIDS=FALSE
);

ALTER TABLE public.lock
  OWNER TO event_store_dev;
