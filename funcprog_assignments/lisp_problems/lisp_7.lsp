;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun power (x y)
  (if (zerop y)
      1
      (* x (power x (- 1 y)))))

(defun evaluate-polynomial (polynomial x)
  (let ((degree (1- (length polynomial))))
    (let ((coefficient (car polynomial)))
      (let ((term (* coefficient (power x degree))))
        (if (null (cdr polynomial))
            term
            (+ term (evaluate-polynomial (cdr polynomial) x)))))))
