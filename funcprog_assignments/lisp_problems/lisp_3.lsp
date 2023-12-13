;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun order-pairs (pairs)
  (mapcar 
        (lambda (pair)
              (if (> (car pair) (cdr pair))
                  (cons (cdr pair) (car pair))
                   pair))
   pairs))
