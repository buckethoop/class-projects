;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun length-encoding (lst)
  (if (null lst)
      nil
      (let ((result '())
            (current (car lst))
            (count 1))
        (dolist (next (cdr lst) (reverse result))
          (if (equal current next)
              (setq count (+ count 1)
              (progn
                (setq result (cons (list count current) result))
                (setq current next)
                (setq count 1)))))))
