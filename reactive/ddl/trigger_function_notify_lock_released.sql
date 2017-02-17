-- Function: public.notify_lock_acquired()

-- DROP FUNCTION public.notify_lock_acquired();

CREATE OR REPLACE FUNCTION public.notify_lock_released()
  RETURNS trigger AS
$BODY$BEGIN
        NOTIFY released, 'fired by NOTIFY';
        RETURN OLD;
END; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

ALTER FUNCTION public.notify_lock_released()
  OWNER TO event_store_dev;
