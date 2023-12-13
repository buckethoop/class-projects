;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun sum-pair-elements (pairs)
  (let ((sum-first 0)
        (sum-second 0))
    (dolist (pair pairs)
      (setq sum-first (+ sum-first (car pair)))
      (setq sum-second (+ sum-second (cdr pair))))
    (cons sum-first sum-second)))
