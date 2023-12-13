;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun square (x)
  (if (zerop x)
      0
      (+ (square (- x 1)) (+ x (- x 1)))))
