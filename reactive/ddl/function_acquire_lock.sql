CREATE OR REPLACE FUNCTION public.fn_acquire_lock(
    v_lock_domain text,
    v_hostname text,
    v_process_id integer
    ) RETURNS TIMESTAMP AS
$$
BEGIN
    INSERT INTO public.lock (
        lock_domain,
        hostname,
        process_id,
        acquired_at,
        retained_at
    ) VALUES (
        v_lock_domain,
        v_hostname,
        v_process_id,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );
    RETURN CURRENT_TIMESTAMP;
END
$$
  LANGUAGE 'plpgsql';

ALTER FUNCTION public.fn_acquire_lock(
    v_lock_domain text,
    v_hostname text,
    v_process_id integer
    )
  OWNER TO event_store_dev;
