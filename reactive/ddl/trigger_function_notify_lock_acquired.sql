-- Function: public.notify_lock_acquired()

-- DROP FUNCTION public.notify_lock_acquired();

CREATE OR REPLACE FUNCTION public.notify_lock_acquired()
  RETURNS trigger AS
$BODY$BEGIN
        NOTIFY acquired, 'fired by NOTIFY';
        RETURN NEW;
END; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

ALTER FUNCTION public.notify_lock_acquired()
  OWNER TO event_store_dev;
