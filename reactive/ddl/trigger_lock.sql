-- Trigger: trigger_lock_acquired on public.lock

-- DROP TRIGGER trigger_lock_acquired ON public.lock;

CREATE TRIGGER trigger_lock_acquired
  AFTER INSERT OR UPDATE
  ON public.lock
  FOR EACH ROW
  EXECUTE PROCEDURE public.notify_lock_acquired();

-- Trigger: trigger_lock_released on public.lock

DROP TRIGGER trigger_lock_released ON public.lock;

CREATE TRIGGER trigger_lock_released
  AFTER DELETE
  ON public.lock
  FOR EACH ROW
  EXECUTE PROCEDURE public.notify_lock_released();

