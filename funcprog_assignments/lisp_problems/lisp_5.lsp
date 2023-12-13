;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun sum-pairs (pairs)
  (mapcar (lambda (pair) (+ (car pair) (cdr pair))) pairs))
