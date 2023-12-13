;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun power (x y)
  (if (zerop y)
      1
      (* x (power x (- y 1)))))
